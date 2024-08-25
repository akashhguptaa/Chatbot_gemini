function getBotResponse() {
    var rawText = $("#textInput").val();
    
    // Display user's text
    var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document
      .getElementById("userInput")
      .scrollIntoView({ block: "start", behavior: "smooth" });
  
    // Create a placeholder for the bot response
    var botHtml = '<p class="botText"><span id="botResponse"></span></p>';
    $("#chatbox").append(botHtml);
  
    // Establish an EventSource connection to stream responses
    var source = new EventSource("/get?msg=" + encodeURIComponent(rawText));
    var isResponseComplete = false;
  
    source.onmessage = function (event) {
      // Accumulate the response in the same message box
      var currentText = $("#botResponse").html();
      $("#botResponse").html(currentText + event.data);
      document
        .getElementById("userInput")
        .scrollIntoView({ block: "start", behavior: "smooth" });
    };
  
    source.onerror = function () {
      source.close();
      if (!isResponseComplete) {
        // Mark the end of the response
        $("#botResponse").attr("id", "");
        isResponseComplete = true;
      }
    };
  
    source.onopen = function () {
      // Once the connection is open, make sure to handle it
      source.onmessage = function (event) {
        // Append the data to the existing response box
        var currentText = $("#botResponse").html();
        $("#botResponse").html(currentText + event.data);
        document
          .getElementById("userInput")
          .scrollIntoView({ block: "start", behavior: "smooth" });
      };
  
      source.onerror = function () {
        // When the stream ends, mark the response as complete
        $("#botResponse").attr("id", "");
        source.close();
        isResponseComplete = true;
      };
    };
  }
  
  $("#textInput").keypress(function (e) {
    if (e.which == 13) {
      getBotResponse();
    }
  });
  