---
layout: home
---

<div class="index-content coding">
  <div class="section">
    <ul class="artical-cate">
      <li class="on"><a href="/coding"><span>程序人生</span></a></li>
      <li><a href="/life"><span>生活随笔</span></a></li>
      <li><a href="/resume"><div class="new"><span>个人简历</span></div></a></li>
      <li><a href="/jsoneditor" target="_blank"><span>JSONEditor</span></a></li>
    </ul>

    <div class="cate-bar"><span id="cateBar"></span></div>

    <ul class="artical-list">
      {% for post in site.categories.coding %}
      <li>
        <div class="table-article">
          <div class="col-title">
            <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
          </div>
          <div class="col-date">
            <p class="entry-date">{{ post.date|date:"%Y-%m-%d" }}</p>
          </div>
        </div>
        <div class="title-desc">{{ post.description }}</div>
      </li>
      {% endfor %}
    </ul>
  </div>
  <div class="aside">
  </div>

</div>
