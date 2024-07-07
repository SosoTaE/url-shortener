async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

const TEXT_1 = "Welcome to URL Shortener, where we simplify long, complex web addresses into shorter, more manageable links. Our intuitive tool is designed to enhance your online experience by transforming lengthy URLs into easy-to-share links across platforms."
const TEXT_2 = "Simplify sharing, improve accessibility, and make every click more efficient with URL Shortener!"
const about = document.getElementById("about")
const about2 = document.getElementById("about2")
async function writeText(text, element){
  words = text.split(" ")
  element.innerText += `${text[0]}`
  for (let i = 1;i < text.length - 1;i++) {
    element.innerHTML += `${text[i]}`
    await sleep(20)
  }
  element.innerText += text[text.length - 1]
}

async function writeTexts() {
  await writeText(TEXT_1, about)
  await writeText(TEXT_2, about2)
}

function is_there_url() {
  const currentUrl = new URL(window.location.href);
  const queryParams = new URLSearchParams(currentUrl.search);
  for (const [key, value] of queryParams) {
    if (key.includes("url")) {
      return true
    }
  }
  return false;
}

function writeTextsWithoutAnimation() {
   about.innerText = TEXT_1
  about2.innerText = TEXT_2
}

if (is_there_url()) {
  writeTextsWithoutAnimation()
}
else {
  writeTexts()
}