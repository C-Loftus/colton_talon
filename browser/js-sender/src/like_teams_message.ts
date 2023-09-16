function click_last_message() {
  const elements = document.querySelectorAll(
    '[class*="fui-ChatMyMessage__body"]'
  );

  if (elements.length > 0) {
    const lastElement = elements[elements.length - 1];
    lastElement.dispatchEvent(
      new MouseEvent("mouseover", {
        bubbles: true,
        cancelable: true,
        view: window,
      })
    );
  }

  let buttonElement = document.querySelector(
    'div[role="toolbar"] button.fui-Button[type="button"]'
  );

  // Check if the button element exists
  if (buttonElement) {
    // cast the element to a HTMLButtonElement
    const button = buttonElement as HTMLButtonElement;
    // Trigger a click event on the button
    button.click();
  }
}

// wait for the page to load
window.addEventListener("load", () => {
  // wait for the page to load
  console.log("test");
  // click the last message
  const elements = document.querySelectorAll(
    '[class*="fui-ChatMyMessage__body"]'
  );

  if (elements.length > 0) {
    const lastElement = elements[elements.length - 1];
    lastElement.dispatchEvent(
      new MouseEvent("mouseover", {
        bubbles: true,
        cancelable: true,
        view: window,
      })
    );
  }
});
