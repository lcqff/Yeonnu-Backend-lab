package jpabook.jpashop.domain;

import java.util.ArrayList;
import java.util.List;
import javax.persistence.Column;
import javax.persistence.Embedded;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToMany;

@Entity
public class Member extends BaseEntity{

  @Id @GeneratedValue
  @Column(name = "MEMBER_ID ")
  private Long id;
  @OneToMany(mappedBy = "member")
  private List<Order> orders = new ArrayList<Order>();
  @Column(length = 10)
  private String name;
  @Embedded
  private Address address;

  public Long getId() {
    return id;
  }

  public String getName() {
    return name;
  }

  public void setId(Long id) {
    this.id = id;
  }

  public List<Order> getOrders() {
    return orders;
  }

  public void setOrders(List<Order> orders) {
    this.orders = orders;
  }

  public void setName(String name) {
    this.name = name;
  }

  public Address getAddress() {
    return address;
  }

  public void setAddress(Address address) {
    this.address = address;
  }

  public static void main(String[] args) {
    System.out.println("Hello world!");
  }
}