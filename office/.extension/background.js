// Function to handle the command event
function handleCommand(command) {
  const teamsBaseUrl = "https://teams.microsoft.com";
  const outlookBaseUrl = "https://outlook.office.com";

  if (command === "focus_or_launch_teams") {
    handleTab(teamsBaseUrl);
  } else if (command === "focus_or_launch_outlook") {
    handleTab(outlookBaseUrl);
  }
}

// Function to handle the tab (focus or create)
function handleTab(url) {
  // Check if the URL is already open in any tab
  chrome.tabs.query({ url: url + "/*" }, function (tabs) {
    if (tabs && tabs.length > 0) {
      // If the URL is already open, focus the first tab
      chrome.tabs.update(tabs[0].id, { active: true });
    } else {
      // If the URL is not open, create a new tab with the URL
      chrome.tabs.create({ url: url });
    }
  });
}

// Listen for command events
chrome.commands.onCommand.addListener(handleCommand);
