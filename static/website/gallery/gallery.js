var gallery_div = document.querySelector('#gallery')

for(var i=0; i<12;i++){
    gallery_div.innerHTML+= `
        <div class='gimg'>
            <img src='/static/website/gallery/img/${i+1}.jpg'>
        </div>
    `
}