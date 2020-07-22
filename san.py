class student:
  def __init__(self, name, USN,per):
    self.name = name
    self.USN = USN
    self.per = per

s1 = student("sanketh", 49, 70)
sank(s1)
s2 = student("sankth", 48, 74)
s3 = student("saneth", 46, 76)
a=0
def sank(s):
    b=s
    if(b.per>a):
        a=s.per
    return a
