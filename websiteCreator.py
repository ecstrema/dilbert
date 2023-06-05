# this file outputs an html file with all the images from the in img tags

import json

with open("data.json", "r") as f:
    data = json.load(f)

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simple Dilbert viewer</title>
  <style>
    * {{
      text-align: center;
    }}

    a {{
      text-decoration: none;
      color: black;
    }}

    h1:hover {{
      text-decoration: underline;
      cursor: pointer;
    }}
  </style>

  <script>
  function onVisible(element, callback) {{
    new IntersectionObserver((entries, observer) => {{
      entries.forEach(entry => {{
        if(entry.intersectionRatio > 0) {{
          callback(element);
          observer.disconnect();
        }}
      }});
    }}).observe(element);
  }}
  </script>
</head>
<body>
{
    "".join([f'''<a href="#{d["date"]}">
<h1 id="{d["date"]}">{d["date"]}</h1>
<img alt="" data-src="{d["img_src"]}" loading="lazy">
</a>''' for d in data])
}

<script>
  const images = document.querySelectorAll("img");
  images.forEach(img => {{
    onVisible(img, (element) => {{
      element.src = element.getAttribute("data-src");
    }});
  }});
</script>
</body>
</html>
"""


with open("index.html", "w") as f:
    f.write(html)
