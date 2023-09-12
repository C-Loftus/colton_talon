(function enableRightClick() {
  // Add an event listener to the document that prevents the contextmenu event
  document.addEventListener("contextmenu", (event) => {
    event.preventDefault();
  });

  console.log("Right-click has been enabled.");
})();