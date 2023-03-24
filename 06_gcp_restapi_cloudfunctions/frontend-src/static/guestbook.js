"use strict";

// fill in your API Gateway endpoint here
const baseApiUrl = "<FMI>"; 

/** Display the guestbook entries
 *
 *  Builds up the webpage by manipulating the DOM.
 *  Clears the children of the div with the id "entries", then adds the new entries
 *  to it. We call this to initialize the page and update when entries are added.
 */
const renderEntries = entries => {
  const entriesNode = document.getElementById("entries");

  while (entriesNode.firstChild) {
    entriesNode.firstChild.remove();
  }

  entries.map(entry => {
    const entryNode = document.createElement("section");
    entryNode.classList.add("entry", "box");
    const email = entry.email ? `&lt;${entry.email}&gt;` : "";
    entryNode.innerHTML = `<pre>${entry.message}</pre>
    <header>
      ${ entry.name } ${email}<br>
      <em>signed on ${entry.signed_on}</em>
    </header>`
    // .strftime("%d.%m.%Y at %H:%M")
    entriesNode.appendChild(entryNode);
  });
};

/** Get the form field values and POST them to the REST API
 *
 *  We send the API JSON and expect the updated entries
 *  in response as JSON.
 *  Display the entries on the page once they arrive.
 */
const sign = async () => {
  const name = document.querySelector("input[name=name]");
  const email = document.querySelector("input[name=email]");
  const message = document.querySelector("textarea[name=message]");
  const button  = document.querySelector("input[type=submit]");
  button.style.display = "none";

  await fetch(baseApiUrl + "entry", {
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json"
    },
    method: "POST",
    body: JSON.stringify({ name: name.value, email: email.value, message: message.value })
  });
  button.style.display = "block";
  name.value = "";
  email.value = "";
  message.value = "";
  getEntries();
};
document.querySelector("input[type=submit]").addEventListener("click", sign);

/** GET the guestbook entries from the REST API
 *
 *  Display them on the page once they arrive.
 */
const getEntries = async () => {
  const entriesNode = document.getElementById("entries");
  entriesNode.innerHTML = "Loading entries...";
  const response = await fetch(baseApiUrl + "entries", {
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json"
    },
    method: "GET"
  });
  const gbentries = await response.json();
  renderEntries(gbentries);
};

// initialize the entries when a new guest arrives
getEntries();
