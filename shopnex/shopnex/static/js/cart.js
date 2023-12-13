let updateBtns = document.getElementByClassName('update-cart')


for (let i = 0; i < updateBtns.lenth; i++) {
  updateBtns[i].addEventListener('click', function(){
    let productId = this.dataset.product
    let action = this.dataset.action
    console.Log('productId:', productId, 'Action:', action)
    console.Log('User:', user)


    if (user == 'AnonymousUser'){
      console.Log('User is not authenticated')

    }else{
      updateUserOrder(productId, action)

    }
  })

}
function addCookieItem(productId, action){
  console.Log('User is not authenticated')

  if (action == 'add'){
    if (cart[productId] == undefined){
      cart[productId] = {'quantity':1}
    }else{
      cart[productId]['quantity'] + 1
    }
  }
  if (action == 'remove'){
    cart[productId]['quantity'] -= 1

    if (cart[productId]['quantity'] <= 0){
      console.Log('remove Item')
      delete cart[productId]
    }
  }
  console.Log('Cart:', cart)
  document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'
  location .reload()
}
if (user == 'AnonymousUser'){
  addCookieItem(productId, action)
}else{
  updateUserOrder(productId, action)

}



function updateUserOrder(productId, action){
  console.log('User is authenticated')
  let url = '/update_item'

  fetch(url, {
    method: 'POST',
    header: {
        'Content-type':'application/json',
        'X-CSRFToken':csrftoken,
    } ,
    body:JSON.stringify({'productId':productId, 'action':action})
  })
  .then((response) => {
    return response.json()
  })
  .then((data) => {
    console.log('data:', data)
    location.reload()
  });
}
