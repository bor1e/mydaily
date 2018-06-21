<section class="hero is-info">
    <div class="hero-body level" id="{{category}}">
        <div class="container">
            <p class="heading">
            %if attr > 1:
               <small>reading time ca. {{!attr}}min</small>
            %else:
                <small>reading time less than a min</small>
            %end
            </p>
            <p class="title">{{!title}}</h1>
            {{!buttons}}
        </div>
    </div>
</section>
<section class="section">
    <div class="content">
        <div class="container">
            {{!content}}
            {{!buttons}}
        </div>
    </div>
</section>
