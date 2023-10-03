// Get all elements with [width='100%'] tr [border='0'] tbody [type='text']
const elements = document.querySelectorAll(
  '[width="100%"] tr [border="0"] tbody [type="text"]'
);

country = true;
elements.forEach((element) => {
  element.value = country ? "United States" : "Massachusetts";
  country = !country;
});

const description = document.querySelectorAll("td textarea");

const defaultDescription = description[0].value;

for (let i = 0; i < description.length; i++) {
  description[i].value = defaultDescription;
}
