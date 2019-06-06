var sponsors_html = document.querySelector('.patreons');
var this_container = document.querySelector('#this_spons')
var this_spons_div = document.querySelector('#this_spons div')

var type = {
  'AS': 'Associate Sponsors',
  'PLTS': 'Platinum Sponsors',
  'GS': 'Gold Sponsors',
  'TS': 'Title Sponsors',
  'PRTS': 'Partner Sponsors',
}

fetch('/sponsors/list/')
  .then(data => data.json())
  .then(function (data) {
    console.log(data)
    this_container.style.display = 'block'
    document.getElementById('spons_head').innerHTML = `Sponsors of E'Summit ${year}`

    if (data.success == true) {
      var sponsors = data.spons;
      var this_spons = []

      sponsors.forEach(type => {
        type.sponsors.forEach(function (sponsor) {
          if (sponsor.year == year) {
            this_spons.push(sponsor)
          }
        })
      })
      insert_sponsors(this_spons, this_spons_div)
    } else {
      this_container.style.display = 'block'
      this_container.innerHTML += `<center><h3>Coming Soon</h3></center>`
    }
    document.querySelector('#spinner').remove();
  })

insert_sponsors = (spons, location) => {
  spons.forEach(function (sponsor) {
    location.innerHTML += ` 
            <div class='sponsor'>
                <img src='${sponsor.pic}'>
                <div class='details'>
                    <h2>${sponsor.name}</h2>
                    <p class='body'>${sponsor.details}</p>
                    <p class='contact_no'>${sponsor.contact}</p>
                    <p class='website'><a href='${sponsor.website}'>website</a></p>
                </div>
            </div>`;
  })
}