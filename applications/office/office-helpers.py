import os
import pathlib

from talon import Module, actions, app, clip, cron, ui

mod = Module()

mod.list("pandoc_output_format", desc="list of pandoc output formats")


def get_output_format(spoken_form: str):
    """gets a list of pandoc output formats"""
    output_ext = ""
    match spoken_form:
        case "docx" | "word" | "doc":
            output_ext = "docx"
        case "pptx" | "powerpoint" | "ppt" | "Powerpoint":
            output_ext = "pptx"
        case "pdf" | "PDF" | "p d f" | "P D F":
            output_ext = "pdf"
        case "html" | "website":
            output_ext = "html"
        case "latex" | "tech" | "tex":
            output_ext = "tex"
        case "_":
            raise ValueError("No output format specified")
    return output_ext


def get_compiled_file_path(full_path: str, output_format: str):
    """returns the path to the compiled file"""
    # get basename without extension
    file_name = os.path.basename(full_path)
    file_name_without_extension = os.path.splitext(file_name)[0]
    output_ext = get_output_format(output_format)

    # get the filename without the last directory
    dirname = os.path.dirname(full_path)

    # get the build directory
    build_dir = os.path.join(dirname, "build")

    compiled_filename = f"{file_name_without_extension}.{output_ext}"

    new_path = os.path.join(build_dir, compiled_filename)

    # actions.user.notify(f"opening {new_path}")
    return new_path


@mod.action_class
class Entrance:
    def email_entrance() -> str:
        """script the intro of an email"""
        res: str = clip.text()
        first = res.split(",")[1].strip()
        return first

    def compile_all_markdown():
        """Compiles all markdown files in the current directory to docx"""

        cmd = r"Get-ChildItem -Filter *.md | ForEach-Object { $outputFile = [System.IO.Path]::ChangeExtension($_.FullName, '.docx'); pandoc -t latex+raw_tex $_.FullName | pandoc -f latex --data-dir=docs/rendering/ -o $outputFile }"

        actions.user.paste(cmd)

        file_name = file_name[:-3]

        #  -t is needed to specify the output format
        cmd = f"pandoc {file_name}.md -t docx -o {file_name}.docx"
        actions.user.paste(cmd)

    def compile_with_pandoc(full_path: str, output_format: str) -> None:
        """Compiles the current markdown file with pandoc"""
        # get just the filename without the .md extension
        file_name = os.path.basename(full_path)
        file_name_without_extension = os.path.splitext(file_name)[0]

        output_ext = get_output_format(output_format)

        #  -t is needed to specify the output format
        output_path = os.path.join(
            os.path.dirname(full_path),
            "build",
            f"{file_name_without_extension}.{output_ext}",
        )

        cmd = f"pandoc '{full_path}' -F mermaid-filter.cmd -o '{output_path}'"
        actions.user.paste(cmd)

    def open_compiled_file(full_path: str, output_format: str):
        """opens the compiled file within the build directory relative to the current markdown file"""
        # get basename without extension
        new_path = get_compiled_file_path(full_path, output_format)

        cmd = f"start '{new_path}'"
        actions.user.paste(cmd)
        actions.key("enter")

    def check_compiled_file(file_name: str, output_format: str, seconds: int = 5):
        """start the program and then kill it after 5 seconds"""
        new_path = get_compiled_file_path(file_name, output_format)
        cmd = f"start '{new_path}'"
        actions.user.paste(cmd)
        actions.key("enter")

        # kill the program after 5 seconds
        def kill_program():
            if (
                "powerpoint" in ui.active_app().name.lower()
                or "word" in ui.active_app().name.lower()
                or "excel" in ui.active_app().name.lower()
            ):
                actions.key("alt-f4")
            else:
                print(
                    "went to kill application but not in one of the open office applications"
                )

        cron.after(f"{seconds}s", kill_program)

    # def compile_powerpoint(file_name: str):
    #     """compiles to pptx"""
    #     # get the filename without the .md extension
    #     file_name = file_name[:-3]

    #     #  -t is needed to specify the output format
    #     cmd= f"pandoc '{file_name}.md' -t pptx -o {file_name}.pptx"
    #     actions.user.paste(cmd)

    # def compile_word(file_name: str):
    #     """compiles to docx"""
    #     # get the filename without the .md extension
    #     file_name = file_name[:-3]

    #     #  -t is needed to specify the output format
    #     cmd= f"pandoc '{file_name}.md' -t docx -o {file_name}.docx"
    #     actions.user.paste(cmd)

    # def open_compiled_word(file_name: str) -> None:
    #     """opens the compiled word file"""
    #     file_name = file_name[:-3]
    #     cmd= f"start '{file_name}.docx'"
    #     actions.user.paste(cmd)

    # def open_compiled_powerpoint(file_name: str) -> None:
    #     """opens the compiled powerpoint file"""
    #     file_name = file_name[:-3]
    #     cmd= f"start '{file_name}.pptx'"
    #     actions.user.paste(cmd)
