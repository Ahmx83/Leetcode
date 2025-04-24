class Solution(object):
    def lemonadeChange(self, bills) -> str:
        """
        :type bills: list[int]
        :rtype: bool
        """

        # cash_register = []
        #
        # for payment in bills:
        #
        #     if payment == 5:
        #         cash_register.append(5)
        #         continue
        #
        #     elif payment == 10:
        #         if 5 not in cash_register:
        #             return False
        #         cash_register.append(10)
        #         cash_register.remove(5)
        #
        #     elif payment == 20:
        #         if 10 in cash_register and 5 in cash_register:
        #             cash_register.append(20)
        #             cash_register.remove(10)
        #             cash_register.remove(5)
        #         elif cash_register.count(5) >= 3:
        #             cash_register.remove(5)
        #             cash_register.remove(5)
        #             cash_register.remove(5)
        #         else:
        #             return False
        # return True

        ...

        # cash_register = {5: 0, 10: 0, 20: 0}
        #
        # for payment in bills:
        #
        #     if payment == 5:
        #         cash_register[5] += 1
        #
        #     elif payment == 10:
        #         if not cash_register[5]:
        #             return False
        #         cash_register[10] += 1
        #         cash_register[5] -= 1
        #
        #     elif payment == 20:
        #         if cash_register[10] and cash_register[5]:
        #             cash_register[10] -= 1
        #             cash_register[5]  -= 1
        #         elif cash_register[5] >= 3:
        #             cash_register[5] -= 3
        #         else:
        #             return False
        #         cash_register[20] += 1
        #
        # return True

        ...

        if bills[0] != 5:
            return False

        five_bills = 0
        ten_bills = 0

        for payment in bills:
            if payment == 5:
                five_bills += 1

            elif payment == 10:
                if not five_bills:
                    return False
                ten_bills += 1
                five_bills -= 1

            elif payment == 20:
                if five_bills and ten_bills:
                    five_bills -= 1
                    ten_bills -= 1
                elif five_bills >= 3:
                    five_bills -= 3
                else:
                    return False

        return True


sol = Solution()
a = sol.lemonadeChange([5,5,5,5,20,20,5,5,20,5])
print(a)

