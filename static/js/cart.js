var updatebtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updatebtns.length; i++){
    updatebtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('ProductId:', productId, 'Action:', action)

        console.log('USER:', user)
        if(user == 'AnonymousUser'){
            console.log('Not logged in')
        }else{
           updateUserOrder(productId, action)
        }
    })
}