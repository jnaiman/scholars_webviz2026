---
layout: week
icon: undraw_team-collaboration_phnf.svg
visible: true
notitle: true
---

# Putting It Together & Where to Go from Here

Connect your Streamlit app and your github.io site (a button, an embedded app, or a project card), then some resources for going further. See [Lecture 5.1](lecture5p1.html) for the code snippets.

Didn't get to the Streamlit app? [Module 4]({{site.baseurl}}/module04/) is self-contained, so you can do it later on your own. And to work on your site and app on your own computer, see [Module 6]({{site.baseurl}}/module06/).

To **embed your app** in a project page, add this to the page's `.md` file (`?embed=true` hides Streamlit's menus):

```html
<iframe src="https://<your-app>.streamlit.app/?embed=true" style="width: 100%; height: 800px; border: none;"></iframe>
```

### Optional Reading and Materials, Extra Resources

1. <a href="https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app">Embedding Streamlit apps</a>
2. <a href="https://docs.streamlit.io/develop/concepts/multipage-apps">Streamlit multi-page apps</a> and <a href="https://streamlit.io/components">Streamlit components</a>
3. <a href="https://altair-viz.github.io/user_guide/interactions/index.html">Altair interactive charts guide</a>
4. Other Jekyll themes: <a href="https://github.com/topics/jekyll-theme">GitHub's jekyll-theme topic</a> -- vega-lite plots work in any of them with the <a href="{{site.baseurl}}/module03/any_site_starter/plot_page.html">vega-embed approach from Module 3</a>
5. Other tools: <a href="https://plotly.com/python/">Plotly</a> / <a href="https://dash.plotly.com/">Dash</a>, <a href="https://quarto.org/">Quarto</a>, <a href="https://observablehq.com/">Observable</a>, <a href="https://huggingface.co/spaces">Hugging Face Spaces</a>
6. {% assign is445 = site.data.class.urls | where: "id", "is445" | first %}<a href="{{ is445.url }}">IS445 online materials</a> -- a whole semester of data viz with Altair, Jekyll and Streamlit
