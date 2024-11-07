class Solution:
    def convert(s: str, numRows: int) -> str:
        # თუ მხოლოდ ერთი სტრიქონია, პასუხი პირდაპირ თვითონ სტრიქონია
        if numRows == 1 or numRows >= len(s):
            return s
        
        # მრავალსტრიქონიანი სიის შექმნა
        rows = [""] * numRows
        curr_row = 0
        going_down = False

        # სტრიქონის სიმბოლოების გადანაწილება
        for char in s:
            rows[curr_row] += char
            # მიმართულების შეცვლა ზემოთ ან ქვემოთ გადასვლისთვის
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            curr_row += 1 if going_down else -1

        # სტრიქონების გაერთიანება ერთიან ტექსტად
        return "".join(rows)


s = "PAYPALISHIRING"
numRows = 3
# Expected output: "PAHNAPLSIIGYIR"

result = Solution.convert(s, numRows)

print(result)