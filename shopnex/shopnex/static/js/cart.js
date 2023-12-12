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
