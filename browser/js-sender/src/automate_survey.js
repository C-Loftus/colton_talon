// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match
// @icon         https://www.google.com/s2/favicons?sz=64&domain=tampermonkey.net
// @grant        none
// ==/UserScript==

(function () {
  "use strict";


  // Append the button to the document

  // Helper function to click a random element with a given class
  function clickRandomClickableCellElement() {
    const elements = document.querySelectorAll('[class*="input"]');
    if (elements.length > 0) {
      const randomIndex = Math.floor(Math.random() * elements.length);
      elements[randomIndex].click();
    }
  }

  // Function to simulate random clicks
  function simulateRandomClicks() {
    setInterval(function () {
      const randomNumber = Math.random();
      if (randomNumber < 0.8) {
        console.log("clicking clickable cell");
        // Click a random element with "clickableCell" in the class
        clickRandomClickableCellElement();
      } else {
        // Click the second element
        document.getElementById("btn_continue").click();
      }
    }, 1000); // Adjust the interval (in milliseconds) as needed
  }

    simulateRandomClicks();
})();
