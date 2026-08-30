// get stripe data
const stripePublicKey = JSON.parse(
    document.getElementById('id_stripe_public_key').textContent
);
const clientSecret = JSON.parse(
    document.getElementById('id_client_secret').textContent
);
// setup stripe
const stripe = Stripe(stripePublicKey);
const elements = stripe.element();
// create card field
const card = elements.create('card');
card.mount('#card-element');