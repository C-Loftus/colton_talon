app: vscode

-

cell run above: 
    user.vscode("notebook.cell.executeCellsAbove")
    user.vscode("jupyter.runallcellsabove.palette")

cell run: 
    user.vscode("notebook.cell.execute")
    user.vscode("jupyter.runcurrentcell")

cell run all:
    user.vscode("notebook.execute")
    user.vscode("jupyter.runallcells")

consume [<number_small>] : 
    times = number_small or 1
    times = times - 1
    user.vscode("notebook.cell.execute")
    user.vscode("notebook.focusNextEditor")

    user.vscode("jupyter.runcurrentcell")
    user.vscode("jupyter.gotoNextCellInFile")

    repeat(times)

jump [<number_small>]:
    times = number_small or 1
    times = times - 1
    user.vscode("notebook.focusNextEditor")

    user.vscode("jupyter.gotoNextCellInFile")
    repeat(times)

export to notebook:
    user.vscode("jupyter.exportfileandoutputasnotebook")

export to python:
    user.vscode("jupyter.exportAsPythonScript")
    user.vscode("workbench.action.files.save")


fall <number_small> :
    user.vscode("notebook.focusPreviousEditor")
    user.vscode("jupyter.gotoPrevCellInFile")
    repeat(number_small-1)


(cell insert | cell new): 
    user.vscode("jupyter.insertCellBelow")
    user.vscode("notebook.cell.insertCodeCellBelow")

cell join above:
    user.vscode("notebook.cell.joinAbove")

cell join below:
    user.vscode("notebook.cell.joinBelow")

split cell:
    user.vscode("notebook.cell.split")

(cell delete | chuck cell):
    user.vscode("notebook.cell.delete")