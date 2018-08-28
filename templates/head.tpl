<section class="hero is-primary is-fullheight">
  <div class="hero-head">
    <p class="heading is-pulled-right">בס"ד</p>
  </div>
  <div class="hero-body">
    <div class="container has-text-centered">
      <div class="column is-6 is-offset-3">
        <h1 class="title">MYDAILY</h1>
        <h2 class="subtitle">
          helps you to organise your <b>Jewish learning</b>.<br> Mydaily will remember where you left, so that you can just continue from there on. Suited for Smartphone use.
        </h2>
      </div>
      <div class="column is-6 is-offset-3">
        <p class="title">Go ahead, learn something:</p>
        <p class="buttons is-centered">
          <a class="button is-info is-rounded" href="#hayomyom">
            HaYomYom
          </a>      
          <a class="button is-info is-rounded" href="#tora">
            Chumasch
          </a>
          <a class="button is-info is-rounded" href="#rambam">
            Rambam
          </a>
          <a class="button is-info is-rounded" href="#tanach">
            Tanach
          </a>
        </p>
      </div>                      
      <div class="column is-6 is-offset-3">
        <p class="is-size-7 has-text-centered">
         provided with texts from <a href="chabad.org">chabad.org</a>
        </p>
      </div>     
      <!--div class="column is-6 is-offset-3">
        <p class="subtitle">Suggest a new Online Source for everyone:</p>
        <div class="box">
          <form action="/new_source" method="POST" onsubmit="confirm()">
            <div class="field is-grouped is-centered">
              <p class="control is-expanded">
                <input class="input" name="new_source" type="text" placeholder="Enter url of book source">
              </p>
              <p class="control">
                <a class="button is-info" type="submit">
                  Suggest new Book
                </a>
              </p>
            </div>
          </form>
        </div>
      </div-->          
    </div>
  </div>
  <div class="hero-foot">
    <nav class="level">
      <div class="level-item has-text-centered">
        <div>
          <p class="heading">Today's estimated Learning</p>
          <p class="title">{{!totaltime}} MIN</p>
        </div>
      </div>
      <div class="level-item has-text-centered">
        <div>
          <span class="tag is-success is-large">
            <a href="https://paypal.me/OnlineShiurim">Support MYDAILY</a>
          </span>
        </div>
      </div>
      <div class="level-item has-text-centered">
        <div>
          <p class="heading">MYDAILY Visitors</p>
          <p class="title">{{!visitors}}</p>
        </div>
      </div>
    </nav>
  </div>
</section>
