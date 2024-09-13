const productos = [
    {
        id:1,
        productName: "Banana",
        price: 480,
        quanty: 1,
        img: "/client/media/bananas.jpeg" 
    },
    {
        id:2,
        productName: "Leche",
        price: 950,
        quanty: 1,
        img: "/client/media/Leche.jpg" 
    },
    {
        id: 3,
        productName: "Pollo",
        price: 750,
        quanty: 1,
        img: "/client/media/pollo.jpeg" 

    }
]


productos.forEach((product)=>{
    const content = document.createElement("div")
    content.innerHTML= ` 
    <img src="${product.img}"/>"
    <h3>${product.productName}</h3>
    <p>${product.price}</p>
    `;
    shopContent.append(content)

    const buyButton = document.createElement("button");
    buyButton.innerText = "Comprar"

    content.append(buyButton)

    buyButton.addEventListener("click", ()=>{
        const repeat = cart.some((repeatProduct) => repeatProduct.id === product.id)

        if(repeat){
            cart.map((prod)=>{
                if(prod.id === product.id){
                    prod.quanty++;
                    displayCartCounter();
                }
            })
        }else{
            cart.push({
                id: product.id,
                productName: product.productName,
                price: product.price,
                quanty: 1,
                img: product.img
            })
            console.log(cart)
            displayCartCounter();
        }
    })
});
