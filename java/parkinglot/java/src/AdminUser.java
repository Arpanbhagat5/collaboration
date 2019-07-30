class AdminUser extends User {
	String memberId;
	
    public AdminUser() {
		this.name = "ADMIN"
		this.contact = "080433333333"
    }
    // public void editVehicleUserData(VehicleUser user) {
        
    // }
    public void makeMember(VehicleUser vUser) {
		memberId = generateMemberId(vUser);
		System.out.println(vUser.name + " has been made member of this parking lot.");
		System.out.println("Your member ID is: " + memberId);
		
    }
    public void removeMember() {
        
    }
	
	public String generateMemberId(VehicleUser vUser) {
		String memberIdPrefix = vUser.name.substring(0,2);
		String memberIdSuffix = vUser.vehicleNumber;
		memberId = memberIdPrefix + memberIdSuffix;
		return memberId;
	}
}