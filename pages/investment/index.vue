<template>
  <div class="main">
    <div class="container">
      <div class="columns"></div>

      <div class="columns">
        <div class="column is-4">
          <logo />
          <div class="columns is-centered">
            <div class="column is-half">
              <nuxt-link
                to="/"
                class="button is-medium is-light center"
                style="margin-top: 25px; "
              >Back</nuxt-link>
            </div>
          </div>
        </div>
        <div class="column is-6">
          <div class="card">
            <header class="card-header">
              <p class="card-header-title">Retirement Investment Calculator</p>
              <a href="#" class="card-header-icon" aria-label="more options">
                <span class="icon">
                  <i class="fas fa-angle-down" aria-hidden="true"></i>
                </span>
              </a>
            </header>
            <div class="card-content">
              <div class="content" style="text-align: left;">
                <div class="columns">
                  <div class="column">
                    <div class="field">
                      <label class="label">Age to Start Investing</label>
                      <div class="control">
                        <input v-model="start_age" class="input" type="text" />
                      </div>
                      <div>
                        <small>Enter a whole number or use slider</small>
                        <br />
                        <div class="range-slider">
                          <div class="badge">18</div>
                          <input
                            v-model="start_age"
                            type="range"
                            min="18"
                            max="100"
                            value="50"
                            class="slider myslider"
                            id="myRange"
                          />
                          <div class="badge">100</div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="column">
                    <div class="field">
                      <label class="label">Age to Retire</label>
                      <div class="control">
                        <input v-model="end_age" class="input" type="text" />
                      </div>
                      <small>Enter a whole number</small>
                      <div class="range-slider">
                        <div class="badge">18</div>
                        <input
                          v-model="end_age"
                          type="range"
                          min="18"
                          max="100"
                          value="50"
                          class="slider myslider"
                          id="myRange"
                        />
                        <div class="badge">100</div>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="columns">
                  <div class="column">
                    <div class="field">
                      <label class="label">Monlthy Contribution</label>
                      <div class="control">
                        <input v-model="monthly" class="input" type="text" />
                      </div>
                      <small>Contribution in Dollars</small>
                      <div class="range-slider">
                        <div class="badge">
                          <small>10</small>
                        </div>
                        <input
                          v-model="monthly"
                          type="range"
                          min="10"
                          max="2000"
                          value="50"
                          class="slider myslider"
                          id="myRange"
                        />
                        <div class="badge">
                          <small>2000</small>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="column">
                    <div class="field">
                      <label class="label">Interest Rate</label>
                      <div class="control">
                        <input v-model="interest" class="input" type="text" />
                      </div>
                      <small>Percent</small>
                      <div class="range-slider">
                        <div class="badge">
                          <small>0</small>
                        </div>
                        <input
                          v-model="interest"
                          type="range"
                          min="0"
                          step="0.005"
                          max="0.20"
                          value="50"
                          class="slider myslider"
                          id="myRange"
                        />
                        <div class="badge">
                          <small>0.20</small>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="field is-grouped">
                  <div class="control">
                    <button @click="calulate_retirement_investment()" class="button is-link">Calculate</button>
                  </div>
                </div>

                <div v-if="showResult" class="notification is-light">
                  <button
                    @click="showResult = !showResult"
                    class="delete"
                  ></button>
                  <b>Results:</b>
                  In {{ end_age - start_age }} years, a monthly investment of ${{ monthly }}
                  would grow to
                  <b>
                    <u>${{ growth }}</u>
                  </b> at a {{ (interest * 100).toFixed(2) }}% interest rate.
                </div>
              </div>
            </div>
            <footer class="card-footer">
              <a href="#" class="card-footer-item">Explain</a>
            </footer>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Logo from "~/components/Logo.vue";

export default {
  components: {
    Logo,
  },
  data() {
    return {

      monthly: 120,
      start_age: 30,
      end_age: 60,
      interest: 0.04,
      years: 0,
      result: 0.0,
      showResult: false,

    };
  },
  computed: {
    growth() {
      var PMT = this.monthly;
      var i = this.interest / 12;
      var n = (this.end_age - this.start_age) * 12;

      // Formula for monthly retirement investment
      var FVA = PMT * ((Math.pow(1 + i, n) - 1) / i);
      this.result = FVA;
      console.log(FVA);
      this.years = this.end_age - this.start_age
      this.showResult = true;
      return this.result.toFixed(2);
    }
  },
  methods: {
    calulate_retirement_investment() {
      var PMT = this.monthly;
      var i = this.interest / 12;
      var n = (this.end_age - this.start_age) * 12;

      // Formula for monthly retirement investment
      var FVA = PMT * ((Math.pow(1 + i, n) - 1) / i);
      this.result = FVA;
      console.log(FVA);
      this.years = this.end_age - this.start_age
      this.showResult = true;
    },

    calculate_desired_pmt() {
      console.log("Calculating Desired Payment");
      var n = 0.0;
      console.log("n", n);
      var PV = this.payment_pv;
      console.log("PV", PV);
      var r = this.payment_interest / 12;
      console.log("r", r);
      var P = this.payment_payment;
      console.log("P", P);

      // Do Calculation
      n = Math.log(Math.pow(1 - (PV * r) / P, -1)) / Math.log(1 + r);
      this.payment_result = n;
      this.showResultDesiredPayment = true;
    },

    calculate_desired_periods() {
      // Setup Vars
      var years = this.period_years;
      var n = years * 12;
      var interest = this.period_interest;
      var i = interest / 12;

      var PVa = this.period_pv;

      // Solve for A
      var A = (i * PVa) / (1 - Math.pow(1 + i, -n));
      this.period_result = A;

      this.showResultDesiredPeriod = true;
    }
  }
};
</script>

<style>
.range-wrapper {
  padding: 0px 8px 0px 8px;
}
.range-slider {
  display: flex;
  justify-content: space-between;
  column-gap: 8px;
  margin-top: 2px;
}

.myslider {
  width: 100%;
  /* padding-left: 8px;
  padding-right: 8px; */
}

.badge {
  padding: 4px 8px 4px 8px;
  border-radius: 4px;
  background-color: whitesmoke;
}

.main {
  padding: 100px;
}

@media (max-width: 592px) {
  .main {
    padding: 25px;
  }
}

/* .container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
} */

@media (min-width: 592px) {
  .title {
    font-family: "Quicksand", "Source Sans Pro", -apple-system,
      BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial,
      sans-serif;
    display: block;
    font-weight: 300;
    font-size: 100px;
    color: #35495e;
    letter-spacing: 1px;
  }
}

@media (max-width: 592px) {
  .title {
    font-family: "Quicksand", "Source Sans Pro", -apple-system,
      BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial,
      sans-serif;
    display: block;
    font-weight: 300;
    font-size: 60px;
    color: #35495e;
    letter-spacing: 1px;
  }
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
