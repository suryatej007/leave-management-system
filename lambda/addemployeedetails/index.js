const AWS = require("aws-sdk");
var docClient = new AWS.DynamoDB.DocumentClient();
exports.handler = (event, context, callback) => {
var tableName = "LeaveRequestsTable";
var params = {
TableName: tableName,
Item: {
"EmployeeId": event.EmployeeId,
"ApplicantEmail": event.ApplicantEmail,
"LeaveDates": event.LeaveDates,
"Status":'Pending',
}
};
docClient.put(params, function (err, data) {
if (err) {
callback(err, data);
}
else {
callback(null, "sucessfully updated data")
}
})
};