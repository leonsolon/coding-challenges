class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accounts.sort()
        dict_accounts = {}
        for account in accounts:
            if account[0] in dict_accounts:
                dict_accounts[account[0]].append(set(account[1:]))
            else:
                dict_accounts[account[0]] = [set(account[1:])]

        for name, account_emails in dict_accounts.items():
            i = 0
            j = 1
            last_len = len(account_emails)
            # print(account_emails)
            while True:
                # print(i,j)
                if i < len(account_emails) and j < len(account_emails) and len(
                        account_emails[i].intersection(account_emails[j])) > 0:
                    account_emails[i] = account_emails[i].union(account_emails[j])
                    account_emails.pop(j)
                    # print('intersection', account_emails)
                else:
                    j += 1

                if j >= len(account_emails):
                    # print('j fora')
                    i += 1
                    j = i + 1
                    if i >= len(account_emails):
                        # print('i fora')
                        if last_len == len(account_emails):
                            # print('sem alteração')
                            break
                        else:
                            # print('houve alteração')
                            i = 0
                            j = 1
                            last_len = len(account_emails)

        result = []
        for name, account_emails in dict_accounts.items():
            for emails in account_emails:
                list_emails = list(emails)
                list_emails.sort()
                result.append([name] + list_emails)

        # print(result)

        return result
