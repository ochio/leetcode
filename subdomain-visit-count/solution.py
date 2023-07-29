from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)

        for i in range(len(cpdomains)):
            times, domain = cpdomains[i].split(" ")
            times = int(times)
            domains = domain.split(".")
            l1 = domains[-1]
            l2 = ".".join(domains[-2:])
            d[l1] += times
            d[l2] += times
            if len(domains) == 3:
                l3 = ".".join(domains)
                d[l3] += times
        
        result = []
        for key, val in d.items():
            result.append(f"{val} {key}")
        return result

