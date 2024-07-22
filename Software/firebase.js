var database = firebase.database();
var dataRef = database.ref("payments");

// Prepare payment data
var paymentData = {
  transactionID: "your_transaction_id",
  // Other payment details
};

// Push payment data to the database
dataRef.push(paymentData);
