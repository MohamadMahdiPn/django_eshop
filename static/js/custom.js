function sendArticleComment(articleId){
    var comment = $('#commentText').val();

    $.get('articles/add-article-comment',{
        articleComment: comment,
        articleId:articleId,
        parentId: null
    }).then(res=>{

    })
}