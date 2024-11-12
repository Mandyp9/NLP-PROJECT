$(document).ready(function() {
    console.log("Document ready");

    var socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.on('connect', function() {
        console.log("Socket connected");
    });

    socket.on('receive_message', function(data) {
        console.log("Message received:", data.message);
        $('#messages').append('<p>' + data.message + '</p>');
        $('#messages').scrollTop($('#messages')[0].scrollHeight); // Auto-scroll
    });

    $('#send-button').click(function() {
        const message = $('#chat-input').val().trim();
        if (message) {
            console.log("Sending message:", message);  // Log before sending
            socket.emit('send_message', {message: message});
            $('#chat-input').val(''); // Clear input
        } else {
            console.log("Empty message, not sent.");
        }
    });

    $('#chat-input').keypress(function(e) {
        if (e.which == 13) { // Enter key
            $('#send-button').click();
            return false; // Prevent default
        }
    });
});
