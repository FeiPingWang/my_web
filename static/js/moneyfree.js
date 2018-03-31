/* 包含大部分web中使用的js */

$(document).ready(function(){
    $("#submit-comment").click(function(){
        console.log("add comment");
        var com = $("#comment-content").val();
        if(com.length != 0)
        {
            $("#tmp").after('<div class="reply-content">' +
            '<div class="topic-author-avater"></div>' +
            '<div class="note-content" id="tmp">' +
            '<span>' + com + '</span></div></div>'
            );
        }
    });
});