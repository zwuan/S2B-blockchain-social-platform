此為 sweartoblock.sol 的解釋文件

以下將此此智能合約分為兩部分 ( 變數意義和函數功能 ) 介紹：

	(一)重要變數
		 1.string public name;
			本變數儲存 swearcoin 名稱，目前是HARD CODE寫死的狀態。
 		 2.6uint8 public decimals = 18;
			 18 精度默認值
  		 3.uint256 public totalSupply;
			不可改動，儲存token的發行總量。

	(二)函數功能
		1.swearToBlock( uint256 initialSupply, string tokenSwear_context ) 
			本智能合約的建構子，僅會在伺服器開始運作時呼叫一次，所有交易都會利用此智能合約。
		2.swear(address _temp, uint256 _value )
			發誓功能，透過用戶間轉帳。_temp放我們自己的錢包地址、_to是見證人地址、_value不可為零
		3.check(address _temp, address _challenger, uint256 _value, bool _complete)
			見證人確認此時才會真的匯款，_temp是我們的錢包地址、 _challenger挑戰者的錢包地址、 _value 挑戰者的下注金額、
			 _complete是否達成發誓。
		4.transfer(address _to, uint256 _value)
			用來處理客戶跟我們買代幣， _to購買人、 _value購買量。
		5.swearToBlock( uint256 initialSupply )
			建構子，輸入的數字代表我們的token的總數乘以10^18。例如輸入5，則token總數為 5000000000000000000