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
        location.reload();
    })
}

function fillParentId(parentId) {
    $('#parentId').val(parentId);
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});
}
