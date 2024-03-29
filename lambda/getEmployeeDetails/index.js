const AWS = require('aws-sdk');
var docClient = new AWS.DynamoDB.DocumentClient();
var tableName = "LeaveRequestsTable";
exports.handler = (event, context, callback) => {
var params = {
TableName: tableName,
Key: {
"EmployeeId": event.EmployeeId
}
}
docClient.get(params, function (err, data) {
callback(err, data.Item);
})
};