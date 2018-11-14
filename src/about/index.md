---
layout: about
---

<section class="about-me">
<h2 class="about-h2 md-p-center">我是谁</h2>
<hr>
<p class="about-content">我叫徐韬，前阿里巴巴高级技术专家，现同家人在美国华盛顿(北弗吉尼亚)居住。</p>
<p class="about-content">My name is Tao(Jason) Xu, I am a former tech lead(senior technologist) with Aliabba Group. Currently I'm living with my family in Washington, D.C. area</p>

<div class="md-flex-v about-contact">
    <div><i class="fas fa-envelope"></i> | taoxu.dev@gmail.com </div>
    <div><i class="fab fa-linkedin-in"></i> | <a href="https://www.linkedin.com/in/ta0xu/">Tao Xu</a></div>
        <div><i class="fab fa-github"></i> | <a href="https://github.com/xta0">xta0</a></div>
    <div><i class="fab fa-twitter"></i> | <a href="https://twitter.com/ecs_tee">xta0</a></div>
</div>
<!-- <div class="md-flex-h">
    <div class="md-flex-v about-contact">
        <div><i class="fas fa-envelope"></i> | taoxu.dev@gmail.com </div>
        <div><i class="fab fa-linkedin-in"></i> | <a href="https://www.linkedin.com/in/ta0xu/">Tao Xu</a></div>
    </div>
    <div class="md-flex-v about-contact">
        <div><i class="fab fa-github"></i> | <a href="https://github.com/xta0">xta0</a></div>
        <div><i class="fab fa-twitter"></i> | <a href="https://twitter.com/ecs_tee">xta0</a></div>
    </div>
</div> -->
</section>


<section class="about-exp">
    <h2 class="md-p-center about-h2">工作经历</h2>
    <hr>
    <div class="md-flex-h md-flex-no-wrap about-exp-item">
        <div  class="about-logo-wrapper">
            <img class="about-logo" src="{{site.baseurl}}/assets/images/about/alipay-logo.png" width="68px">
        </div>
        <ul class="md-margin-left-24">
            <li><strong>高级技术专家-P8 </strong></li>
            <li>蚂蚁金服 | 口碑</li>
            <li>2015年4月 - 2017年9月</li>
            <li>管理口碑iOS研发团队15人 | 业务架构师 </li>
            <ul>
                <li>业务架构设计与系统架构优化</li>
                <li>节日，双12大促稳定性保障与应急</li>
                <li>团队管理，梯队建设，人才招聘，新人培训</li>
            </ul>
            <li>移动端动态发布系统(MIST)设计</li>
            <ul>
                <li>解决App动态更新问题</li>
                <li>端到端系统链路设计</li>
                <li>客户端引擎架构设计/核心代码编写</li>
            </ul>
            <li>Growth Hacking</li>
            <ul>
                <li>数据挖掘方案设计</li>
                <li>数据可视化</li>
            </ul>
        </ul>
    </div>
    <div class="md-flex-h md-flex-no-wrap about-exp-item">
        <div>
            <img src="{{site.baseurl}}/assets/images/about/tdd-logo.png" width="68px">
        </div>
        <ul class="md-margin-left-24">
            <li><strong>无线技术专家-P7 </strong></li>
            <li>阿里巴巴 | 淘点点</li>
            <li>2013年12月 - 2015年4月</li>
            <li>淘点点客户端架构设计</li>
            <li>工具研发</li>
            <li>Scrum敏捷开发</li>
        </ul>
    </div>
    <div class="md-flex-h md-flex-no-wrap about-exp-item">
        <div class="about-logo-wrapper">
            <img src="{{site.baseurl}}/assets/images/about/tb-logo.png" width="68px">
        </div>
        <ul class="md-margin-left-24">
            <li><strong>高级研发工程师-P6</strong></li>
            <li>2012年2月 - 2013年12月</li>
            <li>阿里巴巴 | 手机淘宝 | 一淘 | 一淘逛街 </li>
            <li>日常需求研发, 项目管理</li>
            <li>2013年双11天猫插件研发与集成</li>
        </ul>
    </div>
</section>
<section class="about-github">
    <h2 class="md-p-center about-h2">Github </h2>
    <hr>
    <div class="md-flex-h md-flex-no-wrap">
        <div class="about-logo-wrapper">
            <img class="about-logo" src="{{site.baseurl}}/assets/images/about/mist-logo.png" width="68px">
        </div>
        <ul class="md-margin-left-24">
            <li><a href="https://github.com/Vizzle/MIST"><strong>MIST</strong></a> allows iOS developer to create native UI with JSON templates.</li>
            <li>Features</li>
                <ul>
                    <li>CSS properties and Flexbox layout algorithm</li>
                    <li>Custom expression for handling complex logic</li>
                    <li>Asynchronous rendering technique</li>
                    <li>VSCode Extension for code highlight and lint</li>
                    <li>Development tools support</li>
                </ul>
            <li>With backend involved, MIST let us continuously add new features to our app without submiting to Appstore, by simply downloading the new JSON templates from our CDN nodes and then rendering the page dynamically.</li>
            <li>MIST has been heavily used to implement O2O features in Alipay Wallet since 2016. It has been battle tested and proved stable for more than two years with millions of users visit per day. 
            </li>
        </ul>
    </div>
    <div class="md-flex-h md-flex-no-wrap">
        <div  class="about-logo-wrapper"><img class="about-logo" src="{{site.baseurl}}/assets/images/about/inspector-logo.png" width="68px"></div>
        <div class="about-showcase-p">
            <ul class="md-margin-left-24">
                <li><a hre="https://github.com/xta0/VZInspector"><strong>VZInspector</strong></a> is an iOS in-app runtime debugger.</li>
                <li>Features</li>
                    <ul>
                        <li>Automatically collects all network requests data by hooking the low-level network API </li>
                        <li>View system log messages (e.g. from NSLog).</li>
                        <li>Browses the sandbox files and crash logs</li>
                        <li>Inspect views in the hierarchy</li>
                        <li>Dynamically changing the API enviroment for debugging purpose</li>
                        <li>Many other userful tools</li>
                    </ul>
                <li>VZInspector has been heavily used in our daily development workflow. We use it to track network requests, check the view hierachy, collect performance data for the testing team and do many other insteresting stuff.</li>
            </ul>
        </div>
    </div>
    <div class="md-flex-h md-flex-no-wrap">
        <div  class="about-logo-wrapper">
            <img class="about-logo" src="{{site.baseurl}}/assets/images/about/flex-logo.png" width="68px">
        </div>
        <ul class="md-margin-left-24">
            <li><a href="https://github.com/Vizzle/VZFlexLayout"><strong>FlexLayout</strong></a></li>  
            <li>FlexLayout is a declaretive UI framework in Objective-C++ inspired by   ComponentKit.</li>
            <li>Features</li>
            <ul>
                <li>C++11 aggreate initializer for declaretive APIs</li>
                <li>CSS like properties for UI decoration</li>
                <li>FlexBox Layout Algorithm</li>
            </ul>
            <li> FlexLayout is the core engine of the MIST framework. We implemented our own version of Flexbox algorithm istead of using the open sourced one. Together with MIST, FlexLayout has also been used in Alipay Wallet for more than two years. </li>
        </ul>
    </div>
    <div class="md-flex-h md-flex-no-wrap">
        <div  class="about-logo-wrapper">
            <img class="about-logo" src="{{site.baseurl}}/assets/images/about/vz-logo.png" width="68px">
        </div>
        <ul class="md-margin-left-24">
            <li><a href="https://github.com/Vizzle/Vizzle"><strong>Vizzle</strong></a></li>  
            <li>Vizzle is an iOS MVC framework inspired by Ruby on Rails and Three20.</li>
            <li>Features</li>
            <ul>
                <li>Vizzle takes the idea of "convention over configuration" letting developers write minimium code to make everything work properly</li>
                <li>Vizzle makes a very heavy abstraction for both model and controller layers, Providing the single direciton data flow </li>
                 <li>Vizzle seperates the business layer from the foundation layer using an adapter layer in the middle which  </li>
            </ul>
            <li>Vizzle has been heavily used to implement O2O features in Alipay Wallet and Koubei since 2015. Before that, It had been used in TaoDiandian App for two years. 
            </li>
        </ul>
    </div>
</section>
