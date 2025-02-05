# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        my_domain_count = defaultdict(int)

        for pair in cpdomains:
            count, domain = pair.split()
            count = int(count)
            my_each_d = domain.split(".")
            
            for i in range(len(my_each_d)):
                my_domain_count[".".join(my_each_d[i:])] += count

        return [f"{count} {domain}" for domain, count in my_domain_count.items()]