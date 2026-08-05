const htmlInput = document.getElementById('htmlInput');
const htmlOutput = document.getElementById('htmlOutput');

/**
 * Parses raw input string using DOMParser and renders it into the output element.
 */
function parseAndRender() {
  const rawContent = htmlInput.value;

  // Use DOMParser to safely turn the string into an HTML document tree
  const parser = new DOMParser();
  const parsedDoc = parser.parseFromString(rawContent, 'text/html');

  // Clear existing output
  htmlOutput.innerHTML = '';

  // Append nodes from the parsed body into the output div
  Array.from(parsedDoc.body.childNodes).forEach(node => {
    htmlOutput.appendChild(node.cloneNode(true));
  });
}

// Render immediately as the user types
htmlInput.addEventListener('input', parseAndRender);