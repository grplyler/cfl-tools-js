<template>
  <div class="main">
    <div class="container">
      <div class="columns">
        <div class="column">
          <logo />

          <h1 class="title">Loan Calculator</h1>

          <nuxt-link to="/" class="button is-medium is-light">Back</nuxt-link>
        </div>
      </div>

      <div class="columns">
        <div class="column">
          <div class="card">
            <header class="card-header">
              <p class="card-header-title">Desired Payoff Periods</p>
              <a href="#" class="card-header-icon" aria-label="more options">
                <span class="icon">
                  <i class="fas fa-angle-down" aria-hidden="true"></i>
                </span>
              </a>
            </header>
            <div class="card-content">
              <div class="content" style="text-align: left;">
                <div class="field">
                  <label class="label">Principle Value (PV)</label>
                  <div class="control">
                    <input v-model="period_pv" class="input" type="text" />
                  </div>
                  <small>Current value of the loan</small>
                </div>

                <div class="field">
                  <label class="label">Interest Rate (r)</label>
                  <div class="control">
                    <input v-model="period_interest" class="input" type="text" />
                  </div>
                  <small>Annual Interest Rate</small>
                </div>

                <div class="field">
                  <label class="label">Years (P)</label>
                  <div class="control">
                    <input v-model="period_years" class="input" type="text" />
                  </div>
                </div>

                <div class="field is-grouped">
                  <div class="control">
                    <button @click="calculate_desired_periods()" class="button is-link">Calculate</button>
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
            </div>
            <footer class="card-footer">
              <a href="#" class="card-footer-item">Explain</a>
            </footer>
          </div>
        </div>
        <div class="column">
          <div class="card">
            <header class="card-header">
              <p class="card-header-title">Desired Monthly Payment</p>
              <a href="#" class="card-header-icon" aria-label="more options">
                <span class="icon">
                  <i class="fas fa-angle-down" aria-hidden="true"></i>
                </span>
              </a>
            </header>
            <div class="card-content">
              <div class="content" style="text-align: left;">
                <div class="field">
                  <label class="label">Principle Value (PV)</label>
                  <div class="control">
                    <input
                      v-model="payment_pv"
                      class="input"
                      type="text"
                      placeholder="12000"
                      value="12000"
                    />
                  </div>
                  <small>Current value of the loan</small>
                </div>

                <div class="field">
                  <label class="label">Interest Rate (r)</label>
                  <div class="control">
                    <input
                      v-model="payment_interest"
                      class="input"
                      type="text"
                      placeholder="0.05"
                      value="0.05"
                    />
                  </div>
                  <small>Annual Interest Rate</small>
                </div>

                <div class="field">
                  <label class="label">Desired Payment (P)</label>
                  <div class="control">
                    <input
                      v-model="payment_payment"
                      class="input"
                      type="text"
                      placeholder="220"
                      value="220"
                    />
                  </div>
                </div>

                <div class="field is-grouped">
                  <div class="control">
                    <button @click="calculate_desired_pmt()" class="button is-link">Calculate</button>
                  </div>
                </div>

                <div v-if="showResultDesiredPayment" class="notification is-light">
                  <button
                    @click="showResultDesiredPayment = !showResultDesiredPayment"
                    class="delete"
                  ></button>
                  <b>Results:</b> Loan will be payed off in
                  <u>
                    <b>{{ payment_result.toFixed(2) }} months or {{ (payment_result / 12).toFixed(2) }} years.</b>
                  </u>
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
    Logo
  },
  data() {
    return {
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
      period_result: 0
    };
  },
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

.title {
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

@media (max-width: 592px) {
.title {
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
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
