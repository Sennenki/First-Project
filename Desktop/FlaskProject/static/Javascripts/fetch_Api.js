// # ======================================================================
// #        select to 1st address element
// # ======================================================================

var province_select = document.getElementById('province');
var district_select = document.getElementById('district');
var subDistrict_select = document.getElementById('subDistrict');

// # ======================================================================
// #        select to 2st address element
// # ======================================================================
var other_province_select = document.getElementById('other_province');
var other_district_select = document.getElementById('other_district');
var other_subDistrict_select = document.getElementById('other_subDistrict');


// # ===================================
// #         1st address select
// # ===================================

// # ======  select province  ==============
province_select.addEventListener('focus', e =>{ 
    if(e){
        let province_selected = 'provinces';

        fetch('https://thaiaddressapi-thaikub.herokuapp.com/v1/thailand/' + province_selected)
            .then(response => response.json())
            .then(data => {
                    let optionHTML = '';
                    data.data.map(x => {
                            optionHTML += '<option value="' + x.province + '">' + x.province + '</option>';
                        });
                        province_select.innerHTML = optionHTML;
                    })
    }
});

// // # ======  select district  ==============
province_select.addEventListener('change', e =>{
    var province_selected = province_select.value;
    if(e){
        fetch('https://thaiaddressapi-thaikub.herokuapp.com/v1/thailand/provinces/' + province_selected + '/district')
                .then(response => response.json())
                .then(data => {
                        let optionHTML = '';
                        data.data.map(x => {
                                optionHTML += '<option value="' + x + '">' + x + '</option>';
                            });
                            district_select.innerHTML = optionHTML;
                        })
    }
});



// # ======  select subDistrict  ==============
district_select.addEventListener('change', e =>{
    var province_selected = province_select.options[province_select.selectedIndex].text;
    var district_selected = district_select.options[district_select.selectedIndex].text;
    if(e){
        fetch('https://thaiaddressapi-thaikub.herokuapp.com/v1/thailand/provinces/' + province_selected + '/district/' + district_selected)
                .then(response => response.json())
                .then(data => {
                        let optionHTML = '';
                        data.data.map(x => {
                                optionHTML += '<option value="' + x + '">' + x + '</option>';
                            });
                            subDistrict_select.innerHTML = optionHTML;
                        })
    }
});


// # ===================================
// #        2nd address select
// # ===================================


// # ======  select province  ==============
other_province_select.addEventListener('focus', e =>{ 
    if(e){
        let province_selected = 'provinces';

        fetch('https://thaiaddressapi-thaikub.herokuapp.com/v1/thailand/' + province_selected)
            .then(response => response.json())
            .then(data => {
                    let optionHTML = '';
                    data.data.map(x => {
                            optionHTML += '<option value="' + x.province + '">' + x.province + '</option>';
                        });
                        other_province_select.innerHTML = optionHTML;
                    })
    }
});


// # ======  select district  ==============
other_province_select.addEventListener('change', e =>{
    var province_selected = other_province_select.options[other_province_select.selectedIndex].text;
    if(e){
        fetch('https://thaiaddressapi-thaikub.herokuapp.com/v1/thailand/provinces/' + province_selected)
                .then(response => response.json())
                .then(data => {
                        let optionHTML = '';
                        data.data.map(x => {
                                optionHTML += '<option value="' + x.district + '">' + x.district + '</option>';
                            });
                            other_district_select.innerHTML = optionHTML;
                        })
    }
});


// # ======  select subDistrict ==============
other_district_select.addEventListener('change', e =>{
    var province_selected = other_province_select.options[other_province_select.selectedIndex].text;
    var district_selected = other_district_select.options[other_district_select.selectedIndex].text;
    if(e){
        fetch('https://thaiaddressapi-thaikub.herokuapp.com/v1/thailand/provinces/' + province_selected + '/district/' + district_selected)
                .then(response => response.json())
                .then(data => {
                        let optionHTML = '';
                        data.data.map(x => {
                                optionHTML += '<option value="' + x + '">' + x + '</option>';
                            });
                            other_subDistrict_select.innerHTML = optionHTML;
                        })
    }
});