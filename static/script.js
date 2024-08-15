function getBotResponse() {
    var rawText = $("#textInput").val();
    var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document
      .getElementById("userInput")
      .scrollIntoView({ block: "start", behavior: "smooth" });
  
    var source = new EventSource("/get?msg=" + encodeURIComponent(rawText));
  
    source.onmessage = function (event) {
      var botHtml = '<p class="botText"><span>' + event.data + "</span></p>";
      $("#chatbox").append(botHtml);
      document
        .getElementById("userInput")
        .scrollIntoView({ block: "start", behavior: "smooth" });
    };
  
    source.onerror = function () {
      source.close();
    };
  }
  
  $("#textInput").keypress(function (e) {
    if (e.which == 13) {
      getBotResponse();
    }
  });
  