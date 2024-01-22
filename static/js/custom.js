function sendArticleComment(articleId){
    var comment = $('#commentText').val();
    var parentId = $('#parentId').val();
    console.log(articleId)
    console.log(comment)
    $.get('/articles/add-article-comment',{
        articleComment: comment,
        articleId:articleId,
        parentId: parentId
    }).then(res=>{
        console.log(res);
        $('#commentsArea').html(res)
        $('#commentText').val('');
        $('#parentId').val('');

        if (parentId !== null && parentId !==''){
             document.getElementById('singleCommentBox_'+parentId).scrollIntoView({behavior: "smooth"});
        }
        else{
            document.getElementById('commentsArea').scrollIntoView({behavior: "smooth"});
        }
    })
}

function fillParentId(parentId) {
    $('#parentId').val(parentId);
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});
}
