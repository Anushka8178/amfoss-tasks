chrome.action.onClicked.addListener(async () => {
    chrome.windows.create({
      url: "popup.html",
      type: "popup",
      width: 400,
      height: 400,
    });
  });