function profile_click()
{
   
   // Get the element by its ID
var profile_dropdown_list = document.getElementById("profile_dropdown_list");


   console.log(profile_dropdown_list)
   
    profile_dropdown_list.classList.add("profile_item");
    profile_dropdown_list.classList.remove("profile_item_disabled");
    

}