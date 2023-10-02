// Get all elements with [width='100%'] tr [border='0'] tbody [type='text']
const elements = document.querySelectorAll(
  '[width="100%"] tr [border="0"] tbody [type="text"]'
);

// for each element, type in the value "Test"
country = true;
elements.forEach((element) => {
  element.value = country ? "United States" : "Massachusetts";
  country = !country;
});

// table tbody tr td[nowrap=''][valign='top'] textarea
const description = document.querySelectorAll("td textarea");


const defaultDescription = description[0].value;
// for each description element, set it to the default description
for (let i = 0; i < description.length; i++) {
  description[i].value = defaultDescription;
}
