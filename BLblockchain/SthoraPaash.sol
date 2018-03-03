pragma solidity ^0.4.0;
contract SthoraPaash {
    string public ContainerType;
    int public Quantity;
    string public Weight;
    string public From;
    string public To;
    string public InvoicePrice;
    string public Description;

    function SthoraPaash(string newContainerType, int newQuantity, string newWeight, string newFrom, string newTo, string newInvoicePrice, string newDescription) public{
        ContainerType = newContainerType;
        Quantity = newQuantity;
        Weight = newWeight;
        From = newFrom;
        To = newTo;
        InvoicePrice = newInvoicePrice;
        Description = newDescription;
    }

    function setContainerType(string newContainerType) public{
        ContainerType = newContainerType;
    }

    function getContainerType() public view returns(string){
        return ContainerType;
    }

}