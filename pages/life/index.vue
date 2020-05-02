<template>
  <div class="main">
    <div class="container">
      <div class="columns"></div>

      <div class="columns">
        <div class="column">
          <logo />
          <div class="columns is-centered">
            <div class="column is-full">
              <div class="columns">
                <div class="column">
                  <nuxt-link
                    to="/"
                    class="button is-medium is-light center"
                    style="margin-top: 25px; "
                  >Back</nuxt-link>
                </div>
                <div class="column is-three-quarters">
                  <div class="notification" style="margin-top: 25px; padding: 12px;">
                    <div class="control">
                      <label class="radio">
                        <input type="radio" name="foobar" />
                        Use Salary
                      </label>
                      <label class="radio">
                        <input type="radio" name="foobar" checked />
                        Use Hourly
                      </label>
                    </div>
                  </div>
                </div>
              </div>

              <div class="columns">
                <div class="column is-two-thirds">
                    <div class="field">
                      <div class="control">
                        <input class="input" type="text" />
                      </div>
                    </div>
                </div>
              </div>

              <div class="notification box is-block" style="margin-top: 25px;">
                <button class="delete"></button>
                <span class="is-size-1">$3,233</span>
                <span>left over each month</span>
              </div>
            </div>
          </div>
        </div>
        <div class="column is-two-thirds">
          <div class="card">
            <header class="card-header">
              <p class="card-header-title">Life Calculator</p>
              <a href="#" class="card-header-icon" aria-label="more options">
                <span class="icon">
                  <i class="fas fa-angle-down" aria-hidden="true"></i>
                </span>
              </a>
            </header>
            <div class="card-content">
              <div class="content" style="text-align: left;">
                <div class="columns is-multiline">
                  <div v-for="f in fields" :key="f.title" class="column is-one-fifth">
                    <div class="field">
                      <label class="label">{{ f.title }}</label>
                      <div class="control">
                        <input v-model="f.value" class="input" type="text" />
                      </div>
                    </div>
                  </div>
                </div>

                <div v-if="showResultDesiredPeriod" class="notification is-light">
                  <button
                    @click="showResultDesiredPeriod = !showResultDesiredPeriod"
                    class="delete"
                  ></button>
                  <b>Results:</b>
                  A monthly payment of
                  <b>
                    <u>${{ period_result.toFixed(2) }}</u>
                  </b>
                  will be required to pay off the loan in {{ period_years }} years.
                </div>
              </div>

              <div class="field is-grouped">
                <div class="control">
                  <button @click="calculate_desired_pmt()" class="button is-link">Calculate</button>
                </div>
              </div>

              <div v-if="showFormulas">
                <em>Desired Payoff Periods</em>
                <div
                  v-katex:display="'n = \\frac{\\ln\\bigg[\\Big( 1 - \\frac{PV(r)}{P}\\Big)^{-1}\\bigg]}{\\ln(1+r)}'"
                ></div>
              </div>
            </div>
            <footer class="card-footer">
              <a href="#" class="card-footer-item" @click="showFormulas = !showFormulas">
                <span v-if="showFormulas">Hide Formulas</span>
                <span v-else>Show Forumlas</span>
              </a>
            </footer>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Logo from "~/components/Logo.vue";
import "katex/dist/katex.min.css";

import Vue from "vue";
import VueKatex from "vue-katex";

Vue.use(VueKatex, {
  globalOptions: {
    //... Define globally applied KaTeX options here
  }
});

export default {
  components: {
    Logo
  },
  data() {
    return {
      showFormulas: false,
      showResultDesiredPayment: true,
      showResultDesiredPeriod: false,
      show_explain_periods: false,
      show_explain_payment: false,
      payment_pv: 10000.0,
      payment_interest: 0.05,
      payment_payment: 100.0,
      payment_result: 0.0,
      period_pv: 10000.0,
      period_interest: 0.05,
      period_years: 10,
      period_result: 0,
      hourly_wage: 15,
      weekly_hours: 40,
      salary: 65000,
      hourly_wage: 0,
      weekly_hours: 0,
      rent: 0,
      utilities: 0,
      renters_insurance: 0,
      internet: 0,
      phone: 0,
      car_payment: 0,
      gas: 0,
      car_insurance: 0,
      food_in: 0,
      food_out: 0,
      entertainment: 0,
      internet_subscriptions: 0,
      health_insurance: 0,
      other_monthly: 0,
      fields: [
        {
          title: "Salary",
          value: 65000
        },
        {
          title: "Hourly Wage",
          value: 15
        },
        {
          title: "Weekly Hours",
          value: 40
        },
        {
          title: "Rent",
          value: 800
        },
        {
          title: "Utilities",
          value: 300
        },
        {
          title: "Internet",
          value: 75
        },
        {
          title: "Phone",
          value: 95
        },
        {
          title: "Car Payment",
          value: 235
        },
        {
          title: "Food In",
          value: 350
        },
        {
          title: "Entertainment",
          value: 60
        },
        {
          title: "Internet Subscriptions",
          value: 45
        },
        {
          title: "Health Insurance",
          value: 55
        },
        {
          title: "Other Monthly",
          value: 0
        }
      ],
      use_salary: false
    };
  },
  mounted() {},
  methods: {
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
