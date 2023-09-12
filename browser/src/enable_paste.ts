function enablePasting() {
  // Remove an event listener that prevents the paste event
  document.removeEventListener("paste", preventPasting);

  console.log("Pasting has been enabled.");
}

function preventPasting(event: Event) {
  event.preventDefault();
}

enablePasting();
