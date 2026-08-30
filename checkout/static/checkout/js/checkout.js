// get stripe data
const stripePublicKey = JSON.parse(
    document.getElementById('id_stripe_public_key').textContent
);
const clientSecret = JSON.parse(
    document.getElementById('id_client_secret').textContent
);
// setup stripe
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
// create card field
const style = {
    base : {
        color: '#d4af37',
        fontSize: '16px',
        '::placeholder': {
            color: '#d4af37'
        }
    },
    invalid: {
        color: '#d4af37'
    }
};
const card = elements.create('card', {style: style, hidePostalCode: true});
card.mount('#card-element');
// Pay button setup
const submitButton = document.getElementById('submit-button');
submitButton.addEventListener('click', function() {
    stripe.confirmCardPayment(clientSecret,{
        payment_method: {
            card: card
        }
    }).then(function(result) {
        if (result.error) {
            document.getElementById('card-errors').textContent = 
            result.error.message;
        } else {
            console.log('Payment successful');
        }
    });
});