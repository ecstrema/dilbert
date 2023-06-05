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
  <link rel="icon" type="image/png"
      href="https://web.archive.org/web/20230313000426im_/https://dilbert.com/assets/packs/images/favicon/favicon-96x96-a0f26560c9b6b16718286105ece26211.png"
      sizes="96x96">
  <meta name="keywords" content="dilbert, dilbert comic strip, dilbert comic viewer, comics, web comics">
  <meta name="description" content="Deadly simple Dilbert viewer">
  <style>
    * {{
      text-align: center;
    }}

    a {{
      text-decoration: none;
      color: black;
    }}

    @media (prefers-color-scheme: dark) {{
      body {{
        background-color: rbg(20 20 30);
        color: white;
      }}

      a {{
        color: white;
      }}
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
