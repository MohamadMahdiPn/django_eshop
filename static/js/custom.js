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

function filterProducts() {
    const filterPrice = $('#sl2').val();
    const start_price = filterPrice.split(',')[0];
    const end_price = filterPrice.split(',')[1];
    $('#start_price').val(start_price);
    $('#end_price').val(end_price);
    $('#filter_form').submit();
}

function fillPage(page) {
    $('#page').val(page);
    $('#filter_form').submit();
}

function showLargeImage(imgSrc){
    $('#show_large_image_modal').attr('href', imgSrc);
    $("#main_image").attr('src', imgSrc)
}

function addToCart(productId){
   const productCount = $('#product-count').val();
    $.get('/order/add_to_cart?product_id='+productId+'&quantity='+productCount).then(res=>{
        alert(res)
    })
}